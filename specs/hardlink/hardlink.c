/*
 * This program was originally written by Jakub Jalunik and called
 * cleanftp. I changed the name to hardlink because it could be used on
 * other areas than an FTP site.
 *
 * $Id: hardlink.c,v 1.1 2004/02/24 23:49:14 dag- Exp $
 */

#include <sys/types.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <string.h>
#include <dirent.h>
#include <fcntl.h>

struct _f;
typedef struct _h {
	struct _h *next;
	struct _f *chain;
	off_t size;
	time_t mtime;
} h;

typedef struct _d {
	struct _d *next;
	char name[0];
} d;

d *dirs;

h *hps[131072];

typedef struct _f {
	struct _f *next;
	ino_t ino;
	dev_t dev;
	unsigned int cksum;
	char name[0];
} f;

inline unsigned int hash(off_t size, time_t mtime)
{
	return (size ^ mtime) & 131071;
}

inline int stcmp(struct stat *st1, struct stat *st2)
{
	return st1->st_mode != st2->st_mode || st1->st_uid != st2->st_uid ||
	       st1->st_gid != st2->st_gid || st1->st_size != st2->st_size ||
	       st1->st_mtime != st2->st_mtime;
}

long long ndirs, nobjects, nregfiles, nmmap, ncomp, nlinks, nsaved;

void doexit(int i)
{
	fprintf(stderr, "\n\n");
	fprintf(stderr, "Directories %lld\n", ndirs);
	fprintf(stderr, "Objects %lld\n", nobjects);
	fprintf(stderr, "IFREG %lld\n", nregfiles);
	fprintf(stderr, "Mmaps %lld\n", nmmap);
	fprintf(stderr, "Comparisons %lld\n", ncomp);
	fprintf(stderr, "Linked %lld\n", nlinks);
	fprintf(stderr, "Saved %lld\n", nsaved);
	exit(i);
}

unsigned int buf[64];
char nambuf1[4096], nambuf2[4096];

void rf (char *name)
{
	struct stat st, st2, st3;
	nobjects++;
	if (lstat (name, &st))
		return;
	if (S_ISDIR (st.st_mode)) {
		d * dp = malloc(sizeof(d) + 1 + strlen (name));
		if (!dp) {
			fprintf(stderr, "\nOut of memory 3\n");
			doexit(3);
		}
		strcpy (dp->name, name);
		dp->next = dirs;
		dirs = dp;
	} else if (S_ISREG (st.st_mode)) {
		int fd, i;
		f * fp, * fp2;
		h * hp;
		char *p, *q;
		unsigned int cksum;
		unsigned int hsh = hash (st.st_size, st.st_mtime);
		nregfiles++;
		fprintf(stderr, "  %s", name);
		fd = open (name, O_RDONLY);
		if (fd < 0) return;
		if (read (fd, buf, 256) != 256) {
			close(fd);
			fprintf(stderr, "\r%*s\r", (int)strlen(name)+2, "");
			return;
		}
		for (i = 0, cksum = 0; i < 64; i++) {
			if (cksum + buf[i] < cksum)
				cksum += buf[i] + 1;
			else
				cksum += buf[i];
		}
		for (hp = hps[hsh]; hp; hp = hp->next)
			if (hp->size == st.st_size && hp->mtime == st.st_mtime)
				break;
		if (!hp) {
			hp = malloc(sizeof(h));
			if (!hp) {
				fprintf(stderr, "\nOut of memory 1\n");
				doexit(1);
			}
			hp->size = st.st_size;
			hp->mtime = st.st_mtime;
			hp->chain = NULL;
			hp->next = hps[hsh];
			hps[hsh] = hp;
		}
		for (fp = hp->chain; fp; fp = fp->next)
			if (fp->cksum == cksum)
				break;
		for (fp2 = fp; fp2 && fp2->cksum == cksum; fp2 = fp2->next)
			if (fp2->ino == st.st_ino && fp2->dev == st.st_dev) {
				close(fd);
				fprintf(stderr, "\r%*s\r", (int)strlen(name)+2, "");
				return;
			}
		if (fp) {
			p = mmap (NULL, st.st_size, PROT_READ, MAP_SHARED, fd, 0);
			nmmap++;
			if (p == (void *)-1) {
				close(fd);
				fprintf(stderr, "\nFailed to mmap %s\n", name);
				return;
			}
		}
		for (fp2 = fp; fp2 && fp2->cksum == cksum; fp2 = fp2->next)
			if (!lstat (fp2->name, &st2) && S_ISREG (st2.st_mode) &&
			    !stcmp (&st, &st2) &&
			    (st2.st_ino != st.st_ino || st2.st_dev != st.st_dev)) {
				int fd2 = open (fp2->name, O_RDONLY);
				if (fd2 < 0) continue;
				if (fstat (fd2, &st2) || !S_ISREG (st2.st_mode)) {
					close (fd2);
					continue;
				}
				ncomp++;
				q = mmap (NULL, st.st_size, PROT_READ, MAP_SHARED, fd2, 0);
				if (q == (void *)-1) {
					close(fd2);
					fprintf(stderr, "\nFailed to mmap %s\n", fp2->name);
					continue;
				}
				if (memcmp (p, q, st.st_size)) {
					munmap (q, st.st_size);
					close(fd2);
					continue;
				}
				munmap (q, st.st_size);
				close(fd2);
				if (lstat (name, &st3)) {
					fprintf(stderr, "\nCould not stat %s again\n", name);
					munmap (p, st.st_size);
					close(fd);
					return;
				}
				st3.st_atime = st.st_atime;
				if (stcmp (&st, &st3)) {
					fprintf(stderr, "\nFile %s changed underneath us\n", name);
					munmap (p, st.st_size);
					close(fd);
					return;
				}
				strcpy (nambuf2, name);
				strcat (nambuf2, ".$$$___cleanit___$$$");
				if (rename (name, nambuf2)) {
					fprintf(stderr, "\nFailed to rename %s to %s\n", name, nambuf2);
					continue;
				}
				if (link (fp2->name, name)) {
					fprintf(stderr, "\nFailed to hardlink %s to %s\n", fp2->name, name);
					if (rename (nambuf2, name)) {
						fprintf(stderr, "\nBad bad - failed to rename back %s to %s\n", nambuf2, name);
					}
					munmap (p, st.st_size);
					close(fd);
					return;
				}
				unlink (nambuf2);
				nlinks++;
				nsaved+=st.st_size;
				fprintf(stderr, "\r%*s\rLinked %s to %s, saved %ld\n", (int)strlen(name)+2, "", fp2->name, name, st.st_size);
				munmap (p, st.st_size);
				close(fd);
				return;
			}
		if (fp)
			munmap (p, st.st_size);
		fp2 = malloc(sizeof(f) + 1 + strlen (name));
		if (!fp2) {
			fprintf(stderr, "\nOut of memory 2\n");
			doexit(2);
		}
		close(fd);
		fp2->ino = st.st_ino;
		fp2->dev = st.st_dev;
		fp2->cksum = cksum;
		strcpy(fp2->name, name);
		if (fp) {
			fp2->next = fp->next;
			fp->next = fp2;
		} else {
			fp2->next = hp->chain;
			hp->chain = fp2;
		}
		fprintf(stderr, "\r%*s\r", (int)strlen(name)+2, "");
		return;
	}
}

int main(int argc, char **argv)
{
	int i;
	char *p;
	d * dp;
	DIR *dh;
	struct dirent *di;
	for (i = 1; i < argc; i++)
		rf(argv[i]);
	while (dirs) {
		dp = dirs;
		dirs = dp->next;
		strcpy (nambuf1, dp->name);
		free (dp);
		strcat (nambuf1, "/");
		p = strchr (nambuf1, 0);
		dh = opendir (nambuf1);
		if (dh == NULL)
			continue;
		ndirs++;
		while ((di = readdir (dh)) != NULL) {
			if (!di->d_name[0])
				continue;
			if (di->d_name[0] == '.') {
				char *q;
				if (!di->d_name[1] || !strcmp (di->d_name, "..") || !strncmp (di->d_name, ".in.", 4))
					continue;
				q = strrchr (di->d_name, '.');
				if (q && strlen (q) == 7 && q != di->d_name) {
					*p = 0;
					fprintf(stderr, "Skipping %s%s\n", nambuf1, di->d_name);
					continue;
				}
			}
			strcpy (p, di->d_name);
			rf(nambuf1);
		}
		closedir(dh);
	}
	doexit(0);
	return 0;
}
