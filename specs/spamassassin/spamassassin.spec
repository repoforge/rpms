# $Id$

# Authority: dag

### FIXME: RPM doesn't seem to allow i386-packages with noarch-subpackages.
# Archs: i386

%define real_name Mail-SpamAssassin

Summary: Spam filter for email which can be invoked from mail delivery agents
Name: spamassassin
Version: 2.63
Release: 0
License: Artistic
Group: System Environment/Daemons
URL: http://spamassassin.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://spamassassin.org/released/Mail-SpamAssassin-%{version}.tar.bz2
Source2: redhat_local.cf
Source3: spamassassin-default.rc
Source4: spamassassin-spamc.rc
Source5: spamassassin.sysconfig
Source10: spamassassin-helper.sh
Source99: filter-requires-spamassassin.sh
Patch0: spamassassin-2.60-servicename.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: %{_arch}
Prereq: /sbin/chkconfig, /sbin/service
BuildRequires: perl(HTML::Parser)
Requires: perl(Mail::SpamAssassin) = %{version}-%{release}

%description
SpamAssassin provides you with a way to reduce if not completely eliminate
Unsolicited Commercial Email (spam) from your incoming email.  It can
be invoked by a MDA such as sendmail or postfix, or can be called from
a procmail script, .forward file, etc.  It uses a genetic-algorithm
evolved scoring system to identify messages which look spammy, then
adds headers to the message so they can be filtered by the user's mail
reading software.  This distribution includes the spamd/spamc components
which create a server that considerably speeds processing of mail.

To enable spamassassin, if you are receiving mail locally, simply add
this line to your ~/.procmailrc:
INCLUDERC=/etc/mail/spamassassin/spamassassin-default.rc

To filter spam for all users, add that line to /etc/procmailrc
(creating if necessary).

%package tools
Summary: Miscellaneous tools and documentation for SpamAssassin
Group: System Environment/Daemons
Requires: perl(Mail::SpamAssassin) = %{version}
BuildArch: %{_arch}

%description tools
Miscellaneous tools and documentation from various authors, distributed
with SpamAssassin. See /usr/share/doc/SpamAssassin-tools-*/.

%package -n perl-Mail-SpamAssassin
Summary: Mail::SpamAssassin -- SpamAssassin e-mail filter Perl modules
Requires: perl >= 5.004, perl(Pod::Usage), perl(HTML::Parser)
Group: Applications/CPAN
BuildArch: noarch

%description -n perl-Mail-SpamAssassin
Mail::SpamAssassin is a module to identify spam using text analysis and
several internet-based realtime blacklists. Using its rule base, it uses a
wide range of heuristic tests on mail headers and body text to identify
``spam'', also known as unsolicited commercial email. Once identified, the
mail can then be optionally tagged as spam for later filtering using the
user's own mail user-agent application.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL \
		PREFIX="%{_prefix}" \
		SYSCONFDIR="%{_sysconfdir}" \
		DESTDIR="%{buildroot}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} spamd/libspamc.so

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	INSTALLMAN1DIR="%{buildroot}%{_mandir}/man1" \
	INSTALLMAN3DIR="%{buildroot}%{_mandir}/man3"

%{__install} -d -m0755 %{buildroot}%{_initrddir} \
			%{buildroot}%{_includedir} \
			%{buildroot}%{_sysconfdir}/mail/spamassassin \
			%{buildroot}%{_sysconfdir}/sysconfig/
%{__install} -m0755 spamd/redhat-rc-script.sh %{buildroot}%{_initrddir}/spamassassin
%{__install} -m0644 spamd/libspamc.so %{buildroot}%{_libdir}
%{__install} -m0644 spamd/libspamc.h %{buildroot}%{_includedir}

%{__install} -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/mail/spamassassin/local.cf
%{__install} -m0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/spamassassin
%{__install} -m0644 %{SOURCE3} %{SOURCE4} %{SOURCE10} %{buildroot}%{_sysconfdir}/mail/spamassassin/

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%{__rm} -rf %{buildroot}%{perl_sitearch}/

%post
if [ $1 -eq 1 ]; then
        /sbin/chkconfig --add spamassassin
fi

if [ -f %{_sysconfdir}/spamassassin.cf ]; then
	%{__mv} %{_sysconfdir}/spamassassin.cf %{_sysconfdir}/mail/spamassassin/migrated.cf
fi

if [ -f %{_sysconfdir}/mail/spamassassin.cf ]; then
	%{__mv} %{_sysconfdir}/mail/spamassassin.cf %{_sysconfdir}/mail/spamassassin/migrated.cf
fi

/sbin/service spamassassin condrestart &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
        /sbin/service spamassassin stop &>/dev/null || :
        /sbin/chkconfig --del spamassassin
fi

%postun
if [ $1 -ne 0 ]; then
	/sbin/service spamassassin condrestart &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc BUGS Changes COPYRIGHT README TRADEMARK USAGE *.txt spamd/README.spamd
%doc %{_mandir}/man1/*
%config %{_initrddir}/*
%{_bindir}/*
%{_libdir}/*.so
%{_includedir}/*.h

%files tools
%defattr(0644, root, root, 0755)
%doc sql tools masses contrib

%files -n perl-Mail-SpamAssassin
%defattr(-, root, root, 0755)
%doc MANIFEST
%doc %{_mandir}/man3/*
%config(noreplace) %{_sysconfdir}/mail/spamassassin/
%config(noreplace) %{_sysconfdir}/sysconfig/*
%{_libdir}/perl5/
%{_datadir}/spamassassin/

%changelog
* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 2.63-0
- Updated to release 2.63.

* Sun Jan 18 2004 Dag Wieers <dag@wieers.com> - 2.62-0
- Updated to release 2.62.
- Added missing BuildRequires. (Dries Verachtert)

* Sat Dec 13 2003 Dag Wieers <dag@wieers.com> - 2.61-1
- Added specific Red Hat procmail changes. (John Mellor)

* Tue Dec 09 2003 Dag Wieers <dag@wieers.com> - 2.61-0
- Updated to release 2.61.

* Wed Sep 24 2003 Dag Wieers <dag@wieers.com> - 2.60-0
- Updated to release 2.60.

* Sun Jun 15 2003 Dag Wieers <dag@wieers.com> - 2.55-2
- Removed the runaway perllocal.pod. (Koenraad Heijlen)

* Sun Jun 01 2003 Dag Wieers <dag@wieers.com> - 2.55-1
- Added DarBuildArchs to work-around the noarch-subpackage.

* Tue May 20 2003 Dag Wieers <dag@wieers.com> - 2.55-0
- Updated to release 2.55.

* Tue May 13 2003 Dag Wieers <dag@wieers.com> - 2.54-0
- Updated to release 2.54.

* Fri Apr 04 2003 Dag Wieers <dag@wieers.com> - 2.53-0
- Updated to release 2.53.

* Tue Mar 25 2003 Dag Wieers <dag@wieers.com> - 2.52-0
- Updated to release 2.52.

* Fri Mar 21 2003 Dag Wieers <dag@wieers.com> - 2.51-0
- Updated to release 2.51.

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 2.50-0
- Updated to release 2.50.

* Fri Feb  7 2003 Dag Wieers <dag@wieers.com> - 2.44-0
- Updated to release 2.44.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 2.43-0
- Initial package. (using DAR)
