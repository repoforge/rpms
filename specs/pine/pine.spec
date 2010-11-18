# $Id$
# Authority: dag
# Upstream: news://comp,mail,pine/

### EL2 ships with pine-4.44-20
%{?el2:# Tag: rfx}

%define pgpver 0.18.0
#%define with_gpgpine	1

%define krb5inc %(/usr/kerberos/bin/krb5-config --cflags | sed -e 's|-I||')
%define krb5lib %(/usr/kerberos/bin/krb5-config --prefix)/%{_lib}
%{?rh62:%define krb5inc %{_usr}/kerberos/include}
%{?rh62:%define krb5lib %{_usr}/kerberos/%{_lib}}

Summary: Commonly used, MIME compliant mail and news reader
Name: pine
Version: 4.64
Release: 3%{?dist}
License: Freely Distributable
Group: Applications/Internet
URL: http://www.washington.edu/pine/

Source0: ftp://ftp.cac.washington.edu/pine/pine%{version}.tar.bz2
Source1: http://www.megaloman.com/~hany/_data/pinepgp/pinepgp-%{pgpver}.tar.gz
Source2: pine.conf
Source3: pine-spellcheck
Source5: flock.c
Source6: pine.conf.fixed

#Patch0: pine-4.58-makefile.patch
#Patch1: http://www.suse.de/~bk/pine/4.64/2006-02-23/bigpatch.diff
Patch2: pine-4.04-noflock.patch
Patch3: pine-4.21-passwd.patch
Patch4: pine-4.21-fixhome.patch
Patch8: pine-4.64-imap-4.7c2-flock.patch
Patch9: pine-4.30-ldap.patch
Patch14: pine-4.55-bogus-lock-warning.patch

Patch21: pine-4.31-segfix.patch
Patch22: pine-4.40-lockfile-perm.patch
Patch32: imap-2000-time.patch

# Do not remove this patch without checking that bugs 23679 and 38399
# _remain_ fixed.  [sic: or face the wrath of angry kernel hackers  ;o) ]
#Patch33: pine-4.33-whitespace.patch

# Change PINE sendmail options to attempt to stop sendmail from logging -bs
# errors
#Patch34: pine-4.33-sendmail-options.patch

# Fix bug #60818
Patch36: pine-4.44-overflow.patch

### Patches from http://www.math.washington.edu/~chappa/pine/
Patch100: pine-4.64-all.patch.gz
Patch101: pinepgp-0.18.0-compile.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, ncurses-devel
BuildRequires: openssl-devel, openldap-devel, krb5-devel
%{!?rh62:BuildRequires: pam-devel}
%{?rh62:BuildRequires: pam}

Requires: krb5-libs, mailcap

%description
Pine is a very popular, easy to use, full-featured email user agent
that includes a simple text editor called pico. Pine supports MIME
extensions and can also be used to read news. Pine also supports IMAP,
mail, and MH style folders.

%prep
%setup -n %{name}%{version} -a 1

#%patch0 -p1 -b .makefile
%{__perl} -pi.makefile -e 's|(BASECFLAGS)="-g (.*)"|$1="$2 %{optflags}"|g' imap/src/osdep/unix/Makefile

%{__perl} -pi.redhat-dag -e '
		s|/tmp/.\\usr\\spool\\mail\\|/tmp/.\\var\\spool\\mail\\|g;
		s|/tmp/.&#92;usr&#92;spool&#92;mail&#92;|/tmp/.&#92;var&#92;spool&#92;mail&#92;|g;
	' doc/pine.1 pine/pine.hlp

%{__perl} -pi.redhat-dag -e '
		s|/usr/spool/mail|%{_localstatedir}/spool/mail|g;
		s|/usr/spool/news|/%{_localstatedir}/spool/news|g;
		s|/usr/mail/|%{_localstatedir}/mail/|g;
		s|/usr/local/lib/pine.info|%{_libdir}/pine.info|g;
		s|/usr/local/lib/|%{_sysconfdir}/|g;
		s|/usr/local/bin/|%{_bindir}/|g;
	' doc/pine.1 doc/*.txt doc/tech-notes/*.html pine/osdep/os-*.h pine/pine-use.c pine/init.c pine/pine.hlp

#{__perl} -pi.krb5-dag -e 's|GSSDIR=/usr/local|GSSDIR=/usr/kerberos|' imap/src/osdep/unix/Makefile.gss
%patch4 -p1 -b .fixhome

%{__cp} -p %{SOURCE5} imap/src/osdep/unix

%{__perl} -pi.passwd-dag -e 's|/bin/passwd|%{_bindir}/passwd|;' pine/osdep/os-lnx.h
%patch9 -p1 -b .ldap-patch
%patch14 -p0 -b .bogus-lock-warning

%patch21 -p1 -b .segfix
%patch22 -p0 -b .lockfile-perm

%patch32 -p1 -b .time-h
#%patch33 -p1 -b .whitespace-fix
# This patch does evil things
#%patch34 -p0 -b .sendmail-options
%patch36 -p1 -b .overflow

%patch100 -p1 -b .allpatches
%patch101 -p0 -b .pinegp-compile

# imap flock patch
%patch8 -p0 -b .flock-patch

# this wants /usr/local/bin/perl
#chmod 644 contrib/utils/pwd2pine
%{__perl} -pi -e 's|^#!/.*bin/perl|#!%{__perl}|i' contrib/utils/pwd2pine

%{__rm} -rf krb5 ldap
mkdir krb5 ldap
%{__ln_s} -f %{krb5inc} krb5/include
%{__ln_s} -f %{krb5lib} krb5/lib
%{__ln_s} -f %{_includedir} ldap/include
%{__ln_s} -f %{_libdir} ldap/libraries
./contrib/krb5-setup lnp lnp || :
./contrib/ldap-setup lnp lnp || :

find -name "*.orig" -or -name "*~" | xargs %{__rm} -f core

%build
./build \
	IP="6" \
	OPTIMIZE="%{optflags}" \
	EXTRACFLAGS="-DIGNORE_LOCK_EACCES_ERRORS" \
	EXTRAAUTHENTICATORS="gss" \
	SPECIALAUTHENTICATORS="ssl" \
	SSLTYPE="unix" \
	SSLDIR="%{_prefix}" \
	SSLCERTS="%{_datadir}/ssl" \
	SSLINCLUDE="%{_includedir}/openssl" \
	SSLLIB="-lssl -lcrypto" \
	DEBUG="" \
	lrh

cd pinepgp-%{pgpver}
%configure \
	--with-gpg="%{_bindir}/gpg"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}

%{__make} -C pinepgp-%{pgpver} install-pinegpg \
	DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pine.conf
%{__install} -Dp -m0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/pine.conf.fixed

%{__install} -Dp -m0755 %{SOURCE3} %{buildroot}%{_bindir}/pine-spellcheck
%{__install} -p -m0755 bin/{mailutil,pine,pico,pilot,rpdump,rpload} %{buildroot}%{_bindir}
%{__install} -Dp -m0755 imap/{dmail/dmail,tmail/tmail} %{buildroot}%{_bindir}
%{__install} -Dp -m2755 imap/mlock/mlock %{buildroot}%{_sbindir}/mlock

%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__install} -p -m0644 doc/*.1 imap/src/*/*.1 %{buildroot}%{_mandir}/man1/

%{__mv} -f imap/docs/ imap-docs/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CPYRIGHT README doc/*.txt doc/pine-ports doc/tech-notes/*.html
%doc doc/mailcap.unx doc/mime.types imap-docs/
%doc %{_mandir}/man1/*.1*
%config(noreplace) %{_sysconfdir}/pine.conf*
%{_bindir}/*

%defattr(2755, root, mail, 0755)
%{_sbindir}/mlock

%changelog
* Sun Nov 19 2006 Dag Wieers <dag@wieers.com> - 4.64-3
- Added set of patches from Eduardo Chappa.
- Remove big unicode patch from SuSE.
- Added pinegp compile patch for FC6. (Satish Balay)

* Sun Jul 09 2006 Dag Wieers <dag@wieers.com> - 4.64-2
- Added unicode patch.

* Thu Jan 05 2006 Dag Wieers <dag@wieers.com> - 4.64-1
- Updated to release 4.64.

* Mon May 16 2005 Dag Wieers <dag@wieers.com> - 4.63-1
- Updated to release 4.63.

* Thu Mar 24 2005 Dag Wieers <dag@wieers.com> - 4.62-2
- Fixed ownership of mlock. (Soós Péter)

* Sat Mar 19 2005 Dag Wieers <dag@wieers.com> - 4.62-1
- Updated to release 4.62.

* Sat Aug 14 2004 Bert de Bruijn <bert@debruijn.be> - 4.61-1
- Updated to release 4.61.

* Tue May 18 2004 Dag Wieers <dag@wieers.com> - 4.60-1
- Updated to release 4.60.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 4.58-1
- Added mailutil. (James A Hunsaker)

* Sun Dec 21 2003 Dag Wieers <dag@wieers.com> - 4.58-0
- Initial package. (using DAR)
