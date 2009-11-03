# $Id$
# Authority: dag
# Upstream: <dspam-users$nuclearelephant,com>
# Upstream: Jonathan A. Zdziarski <jonathan$nuclearelephant,com>


Summary: Library and Mail Delivery Agent for Bayesian spam filtering
Name: dspam
Version: 2.10.1
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://dspam.nuclearelephant.com/

Source: http://www.nuclearelephant.com/projects/dspam/sources/dspam-%{version}.tar.gz
Source1: dspam.m4
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: postgresql-python

%{!?dtag:BuildRequires: db4-devel}
%{?el4:BuildRequires: db4-devel}
%{?fc3:BuildRequires: db4-devel}
%{?fc2:BuildRequires: db4-devel}
%{?fc1:BuildRequires: db4-devel}
%{?el3:BuildRequires: db4-devel}
%{?rh9:BuildRequires: db4-devel}
%{?rh8:BuildRequires: db4-devel}
%{?rh7:BuildRequires: db3-devel}
%{?el2:BuildRequires: db3-devel}
%{?rh6:BuildRequires: db3-devel}
Requires: /usr/sbin/useradd

%description
DSPAM (as in De-Spam) is an open-source project to create a new kind of
anti-spam mechanism, and is currently effective as both a server-side agent
for UNIX email servers and a developer's library for mail clients, other
anti-spam tools, and similar projects requiring drop-in spam filtering.

The DSPAM agent masquerades as the email server's local delivery agent and
filters/learns spams using an advanced Bayesian statistical approach (based on
Baye's theorem of combined probabilities) which provides an administratively
maintenance-free, easy-learning Anti-Spam service custom tailored to each
individual user's behavior. Advanced because on top of standard Bayesian
filtering is also incorporated the use of Chained Tokens, de-obfuscation, and
other enhancements. DSPAM works great with Sendmail and Exim, and should work
well with any other MTA that supports an external local delivery agent
(postfix, qmail, etc.)

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__perl} -pi.orig -e 's|\@userdir\@|\$(localstatedir)/lib/dspam|' Makefile.in */Makefile.in

%{__cat} <<EOF >dspam.hourly
#!/bin/sh
cd %{_localstatedir}/lib/dspam
exec >>reprocess.log 2>&1
%{_bindir}/pydspam_process *.spam *.fp
EOF

%{__cat} <<EOF >dspam.daily
#!/bin/sh
%{_bindir}/dspam_clean
EOF

%{__cat} <<EOF >dspam.weekly
#!/bin/sh
%{_bindir}/dspam_purge
EOF

%{__cat} <<EOF >dspam.cgi
#!/bin/sh
cd %{_localstatedir}/www/html/dspam
exec %{_sbindir}/suexec dspam dspam dspam.cgi
EOF

%{__cat} <<EOF >addspam.sh
#!/bin/sh

die() {
  echo `date '+%b%d %H:%M:%S'` "$*" >&2
  exit 1
}

log() {
  echo "$(date '+%b%d %H:%M:%S')" "$*" >&2
}

action="--$(basename $0 .sh)"
log dspam -d $user $action

exec >>%{_localstatedir}/log/dspam.log 2>&1

read from || die "No input"
set - $from
envfrom="$2"
IFS="@"
set - $envfrom
user="$1"
domain="$2"
[ "$domain" = "yourcompany.com" ] || die "Invalid source domain: $domain"
log dspam -d $user $action
%{_bindir}/dspam -d $user $action || die "DSPAM error"
EOF

%{__cat} <<EOF >dspam.conf
ScriptAlias /cgi-bin/ "%{_localstatedir}/www/dspam/cgi-bin/"

<Directory "%{_localstatedir}/www/dspam/cgi-bin">
	AuthName Dspam
	AuthType Basic
#	AuthUserFile /etc/httpd/conf/passwd
#	AuthGroupFile /etc/httpd/conf/group
	Require group dspam
	AllowOverride None
	Options None FollowSymLinks
	Order deny,allow
#	Allow from all
</Directory>
EOF

%build
%configure \
	--disable-dependency-tracking \
	--with-userdir-owner="none" \
	--with-userdir-group="none" \
	--with-dspam-owner="none" \
	--with-dspam-group="none" \
	--enable-homedir-dotfiles \
	--enable-alternative-bayesian \
	--enable-source-address-tracking \
	--enable-client-compression \
	--enable-whitelist \
%{?rh7:--with-storage-driver="libdb3_drv"} \
%{?el2:--with-storage-driver="libdb3_drv"} \
%{?rh6:--with-storage-driver="libdb3_drv"} \
#	--enable-neural-networking

%{__make} %{?_smp_mflags}
%{__mv} -f dspam dspam.optout
%{__rm} -f dspam.o
%{__make} %{?_smp_mflags} dspam \
	CPPFLAGS="-DOPT_IN"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0755 dspam.optout %{buildroot}%{_bindir}/dspam.optout
%{__mv} -f %{buildroot}%{_bindir}/dspam %{buildroot}%{_bindir}/dspam.optin
%{__ln_s} -f dspam.optout %{buildroot}%{_bindir}/dspam

%{__install} -Dp -m0755 addspam.sh %{buildroot}%{_bindir}/addspam
ln -f %{buildroot}%{_bindir}/addspam %{buildroot}%{_bindir}/falsepositive

%{__install} -d -m0755 %{buildroot}%{_includedir}
%{__install} -p -m0644 libdspam.h libdspam_objects.h lht.h nodetree.h %{buildroot}%{_includedir}

%{__install} -Dp -m0755 dspam.hourly %{buildroot}%{_sysconfdir}/cron.hourly/dspam
%{__install} -Dp -m0755 dspam.daily %{buildroot}%{_sysconfdir}/cron.daily/dspam
%{__install} -Dp -m0755 dspam.weekly %{buildroot}%{_sysconfdir}/cron.weekly/dspam

%{__install} -Dp -m0644 dspam.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/dspam.conf

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/mail/
%{__ln_s} -f %{_localstatedir}/lib/dspam %{buildroot}%{_sysconfdir}/mail/dspam

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/smrsh/
%{__ln_s} -f %{_bindir}/addspam %{_bindir}/dspam %{_bindir}/falsepositive %{buildroot}%{_sysconfdir}/smrsh/

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/
touch %{buildroot}%{_localstatedir}/log/dspam.log

%{__install} -Dp -m0755 dspam.cgi %{buildroot}%{_localstatedir}/www/cgi-bin/dspam.cgi
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/dspam/
%{__install} -p -m0755 cgi/*.css cgi/*.cgi cgi/*.gif cgi/*.html %{buildroot}%{_localstatedir}/www/dspam/

%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_datadir}/sendmail-cf/mailer/dspam.m4

%clean
%{__rm} -rf %{buildroot}

%pre
/usr/sbin/useradd -G mail -d "%{_localstatedir}/lib/dspam" -c "Dspam agent" dspam &>/dev/null || :
/usr/sbin/usermod -s /sbin/nologin dspam

if ! grep -q "%{_bindir}/addspam" %{_sysconfdir}/aliases; then
	echo -e "#spam:\t\"|%{_bindir}/addspam\"" >> %{_sysconfdir}/aliases
fi

if ! grep -q "%{_bindir}/falsepositive" %{_sysconfdir}/aliases; then
	echo -e "#spam:\t\"|%{_bindir}/falsepositive\"" >> %{_sysconfdir}/aliases
fi

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc CHANGE LICENSE README RELEASE.NOTES TODO dspam-button.gif txt/*.txt
%config(noreplace) %{_sysconfdir}/cron.hourly/*
%config(noreplace) %{_sysconfdir}/cron.daily/*
%config(noreplace) %{_sysconfdir}/cron.weekly/*
%config(noreplace) %{_sysconfdir}/smrsh/
%config(noreplace) %{_sysconfdir}/mail/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*
%{_bindir}/dspam_crc
%{_bindir}/dspam_clean
%{_bindir}/dspam_merge
%{_bindir}/dspam_2mysql
%{_bindir}/libdb?_purge
#%{_bindir}/dspam_purge.libdb3
%{_bindir}/dspam_purge
%{_bindir}/dspam_corpus
%{_bindir}/dspam_genaliases
%{_datadir}/sendmail-cf/mailer/*
%{_libdir}/*.so.*

%defattr(-, dspam, dspam, 0755)
%{_localstatedir}/www/dspam/

%defattr(0755, root, mail, 0755)
%{_bindir}/addspam
%{_bindir}/dspam
%{_bindir}/dspam_dump
%{_bindir}/dspam_ngstats
%{_bindir}/falsepositive
%{_localstatedir}/www/cgi-bin/dspam.cgi
%{_localstatedir}/lib/dspam/

%defattr(0664, root, mail, 0755)
%{_localstatedir}/log/dspam.log

%defattr(2511, root, mail, 0755)
%{_bindir}/dspam_stats
%{_bindir}/dspam.optin
%{_bindir}/dspam.optout

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.10.1-1.2
- Rebuild for Fedora Core 5.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 2.10.1-1
- Updated to release 2.10.1.

* Sun Mar 14 2004 Dag Wieers <dag@wieers.com> - 2.10.0-1
- Initial package. (using DAR)
