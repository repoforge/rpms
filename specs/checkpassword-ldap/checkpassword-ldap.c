/* checkpassword-ldap
 *
 * checkpassword implementation that searches an LDAP database
 * for all the necessary parameter.
 * 
 * Copyright (C) 2003 Scott James Remnant <scott@netsplit.com>.
 * Copyright (C) 2004 Herve Commowick <hervec@sports.fr>
 *
*/

#include <sys/types.h>

#include <grp.h>
#include <pwd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include <ldap.h>

/* Customise these to change the behaviour.
 * LDAP_HOST		hostname of your LDAP server
 * LDAP_BASE		base under which entry must exist
 * LDAP_SCOPE		search scope relative to base
 * LDAP_FILTER		filter to use, must contain two %s which is replaced with the login name and the domain name
 * LDAP_UID_PARAM	name of field containing uid
 * LDAP_HOME_PARAM	name of field containing emplacement of the mailbox
 * LDAP_BIND_DN		dn of the account who has the good permissions to request search
 * LDAP_BIND_PASSWD	password of the account who has the good permissions to request search
 * MAIL_ACCOUNT_NAME	the name of account who reach the mailbox
 * MAIL_ACCOUNT_UID	the uid of account who reach the mailbox
 * MAIL_ACCOUNT_GID	the gid of account who reach the mailbox
 */

#define LDAP_HOST	"localhost"
#define	LDAP_BASE	"ou=mail,o=enterprise"
#define LDAP_SCOPE	LDAP_SCOPE_SUBTREE
#define LDAP_FILTER	"(&(uid=%s)(dc=%s))"
#define LDAP_UID_PARAM	"uid"
#define LDAP_HOME_PARAM	"mailMessageStore"
#define LDAP_BIND_DN "uid=auth,ou=mail,o=enterprise"
#define LDAP_BIND_PASSWD "password"

#define MAIL_ACCOUNT_NAME "mail"
#define MAIL_ACCOUNT_UID 8
#define MAIL_ACCOUNT_GID 12

#define PROTOCOL_LEN	512

static int  protocol_fd = 3;
char	    up[PROTOCOL_LEN];
char	   *prog, *password, *homeparam, *user, *host, *username;

int _ldap_lookup(void);
int _ldap_get_home_param(void);

int
main (int argc, char *argv[])
{
	struct passwd *pw;
	FILE *protocol;
	int uplen, i;

	prog = argv[0];
	
	protocol = fdopen(protocol_fd, "r");
	if (protocol == NULL) {
		fprintf(stderr, "%s: error opening protocol fd (%d): %s\n",
				prog, protocol_fd, strerror(errno));
		return 100;
		}
	
	uplen = fread(up, 1, PROTOCOL_LEN, protocol);
	
	if (uplen == 0) {
		fprintf(stderr, "%s: bad protocol, zero bytes read\n", prog);
		return 101;
	}

	i = 0;
	username = up + i;
	while (up[i++]) {
		if (i >= uplen) {
			fprintf(stderr, "%s: bad protocol, no username\n",
					prog);
			return 102;
		}
	}

	password = up + i;
	while (up[i++]) {
		if (i >= uplen) {
			fprintf(stderr, "%s: bad protocol, no password\n",
					prog);
			return 103;
		}
	}
	
	for (i = 0, uplen = strlen(username) ; i < uplen ; i++)  
	{
		if (username[i] == '@')
			{
		           user = (char *)malloc(i+1);
		           strncpy(user,username,i);
		           host = (char *)malloc(uplen-i+1);
		           strncpy(host,username +i +1,uplen-i);
			break;
			}
	}
	if ((user == NULL) || (host == NULL))
		return 1;

	if (_ldap_lookup())
		return 1;
	
	if (_ldap_get_home_param())
		return 1;

	free(user);
	free(host);
	free(username);
	
	if (argc <= 1)
		return 0;
	
	if (initgroups(MAIL_ACCOUNT_NAME, MAIL_ACCOUNT_GID) != 0) {
		fprintf(stderr, "%s: unable to set supplementary groups: %s\n",
				prog, strerror(errno));
		return 107;
	}

	if (setgid(MAIL_ACCOUNT_GID) != 0) {
		fprintf(stderr, "%s: unable to set gid : %s\n",
				prog, strerror(errno));
		return 106;
	}
	
	if (setuid(MAIL_ACCOUNT_UID) != 0) {
		fprintf(stderr, "%s: unable to set uid : %s\n",
				prog, strerror(errno));
		return 105;
	}

	if (chdir(homeparam) != 0) {
		fprintf(stderr, "%s: unable to change to home dir (%s): %s\n",
				prog, homeparam, strerror(errno));
		return 108;
	}
	
	execvp(argv[1], argv + 1);
	fprintf(stderr, "%s: unable to exec %s: %s\n", prog, argv[1],
			strerror(errno));
	return 109;
}

int _ldap_lookup(void)
{
	char *attrs[] = { NULL };
	char *filter, *dn;
	char **values;
	LDAP *ld;
	LDAPMessage *res, *entry;
	int ret;

	ld = ldap_init(LDAP_HOST, LDAP_PORT);
	if (!ld) {
		fprintf(stderr, "%s: unable to initialise ldap connection\n",
				prog);
		return 1;
	}

	ret = ldap_simple_bind_s(ld, LDAP_BIND_DN, LDAP_BIND_PASSWD);

	if (ret)
		return 1;

	filter = malloc(sizeof(LDAP_FILTER) + strlen(user) + strlen(host));
	sprintf(filter, LDAP_FILTER, user, host);

	ret = ldap_search_s(ld, LDAP_BASE, LDAP_SCOPE, filter, attrs, 0, &res);
	if (ret) {
		fprintf(stderr, "%s: ldap search failed: %s\n", prog,
				ldap_err2string(ret));
		return 1;
	}

	entry = ldap_first_entry(ld, res);


	if (!entry)
		return 1;

	dn = ldap_get_dn(ld, res);
	
	ldap_msgfree(res);

	ret = ldap_simple_bind_s(ld, dn, password);

	if (ret)
		return 1;

	ldap_memfree(dn);
	ldap_unbind(ld);
	return 0;
}

int _ldap_get_home_param(void)
{
	char *attrs[] = { NULL };
	char *filter, *dn;
	char **values;
	LDAP *ld;
	LDAPMessage *res, *entry;
	int ret;
	
	ld = ldap_init(LDAP_HOST, LDAP_PORT);
	if (!ld) {
		fprintf(stderr, "%s: unable to initialise ldap connection\n",
				prog);
		return 1;
		} 

	ret = ldap_simple_bind_s(ld, LDAP_BIND_DN, LDAP_BIND_PASSWD);
	if (ret)
		return 1;

	filter = malloc(sizeof(LDAP_FILTER) + strlen(user) + strlen(host));
	sprintf(filter, LDAP_FILTER, user, host);
	
	ret = ldap_search_s(ld, LDAP_BASE, LDAP_SCOPE, filter, attrs, 0, &res);

	if (ret) {
		fprintf(stderr, "%s: ldap search failed: %s\n", prog,
				ldap_err2string(ret));
		return 1;
	}
	
	entry = ldap_first_entry(ld, res);
	if (!entry)
		return 1;

	values = ldap_get_values(ld, entry, LDAP_HOME_PARAM);
	if (values && values[0])
		{
		homeparam = malloc(strlen(values[0]) + strlen("../../") + 1);
		strcpy(homeparam,values[0]); 
		strcat(homeparam,"../../");
		}
	ldap_msgfree(res);
	ldap_unbind(ld);
	return 0;
}
