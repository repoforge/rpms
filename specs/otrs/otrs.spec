# $Id$
# Authority: dag
# Upstream: <info$otrs,de>

%{?dtag: %{expand: %%define %dtag 1}}

%define logmsg logger -t %{name}/rpm
%define real_version 2.0.4-01

Summary: Open Ticket Request System
Name: otrs
Version: 2.0.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://otrs.org/

Source: ftp://ftp.otrs.org/pub/otrs/otrs-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#Autoreqprov: no
BuildArch: noarch
Requires: perl, perl-DBI, perl-DBD-MySQL, perl-URI, mod_perl
Requires: perl-Apache-DBI
Requires: mysql, mysql-server, fetchmail, procmail, smtpdaemon
%{?fc4:BuildRequires: httpd}
%{?fc3:BuildRequires: httpd}
%{?fc2:BuildRequires: httpd}
%{?fc1:BuildRequires: httpd}
%{?el3:BuildRequires: httpd}
%{?rh9:BuildRequires: httpd}
%{?rh8:BuildRequires: httpd}
%{?rh7:BuildRequires: apache}
%{?el2:BuildRequires: apache}
%{?rh6:BuildRequires: apache}

%description
OTRS is an Open source Ticket Request System with many features to manage
customer telephone calls and e-mails.

%package docs
Summary: Documentation for package %{name}
Group: Documentation

%description docs
OTRS is an Open source Ticket Request System with many features to manage
customer telephone calls and e-mails.

This package includes the documentation for %{name}.

%prep
%setup -n %{name}

for file in */*.dist */*/*.dist; do
	%{__mv} -f $file $(dirname $file)/$(basename $file .dist)
done

%{__cat} <<EOF >otrs.httpd
ScriptAlias /otrs/ "/opt/otrs/bin/cgi-bin/"
Alias /otrs-web/ "/opt/otrs/var/httpd/htdocs/"

PerlRequire /opt/otrs/scripts/apache2-perl-startup.pl

PerlModule Apache::Reload
PerlInitHandler Apache::Reload

MaxRequestsPerChild 400

<Location /otrs>
#	ErrorDocument 403 /otrs/customer.pl
	ErrorDocument 403 /otrs/index.pl
	AllowOverride All
	SetHandler perl-script
	PerlResponseHandler ModPerl::Registry
	PerlOptions +ParseHeaders
	Options +ExecCGI +FollowSymlinks
</Location>
EOF

%build

%install
%{__rm} -rf %{buildroot}

### Copy with permissions.
%{__install} -Dp -m0710 .fetchmailrc.dist %{buildroot}/opt/otrs/.fetchmailrc
%{__install} -Dp -m0600 .mailfilter.dist %{buildroot}/opt/otrs/.mailfilter
%{__install} -Dp -m0644 .procmailrc.dist %{buildroot}/opt/otrs/.procmailrc

### Copy everything.
%{__cp} -afpv Kernel/ bin/ scripts/ var/ %{buildroot}/opt/otrs/

### Copy with permissions.
%{__install} -p -m0700 bin/DeleteSessionIDs.pl bin/UnlockTickets.pl bin/otrs.getConfig %{buildroot}/opt/otrs/bin/

### Copy extra configuration files.
%{__install} -Dp -m0755 scripts/redhat-rcotrs %{buildroot}%{_initrddir}/otrs
%{__install} -Dp -m0644 scripts/redhat-rcotrs-config %{buildroot}%{_sysconfdir}/sysconfig/otrs
#%{__install} -Dp -m0644 scripts/apache2-httpd.include.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/otrs.conf
%{__install} -Dp -m0644 otrs.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/otrs.conf

touch %{buildroot}/opt/otrs/var/log/TicketCounter.log

### Set permissions.
#%{buildroot}/opt/otrs/bin/SetPermissions.sh %{buildroot}/opt/otrs "otrs" "apache" "apache" "apache"

%pre
if ! /usr/bin/id otrs &>/dev/null; then
        /usr/sbin/useradd -r -d /opt/otrs -s /bin/false -g apache -c 'OTRS System User' otrs || \
                %logmsg "Unexpected error adding user \"otrs\". Aborting installation."
else
	/usr/sbin/usermod -d /opt/otrs otrs
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING INSTALL* README* TODO UPGRADING
%config(noreplace) %{_sysconfdir}/sysconfig/otrs
%config(noreplace) %{_sysconfdir}/httpd/conf.d/otrs.conf
%config %{_initrddir}/otrs
%config(noreplace) /opt/otrs/Kernel/Config.pm
%config(noreplace) /opt/otrs/Kernel/Config/GenericAgent.pm*
#%config(noreplace) /opt/otrs/Kernel/Config/ModulesCusto*.pm
%config(noreplace) /opt/otrs/Kernel/Output/HTML/Standard/
%config(noreplace) /opt/otrs/Kernel/Output/HTML/Lite/
%config(noreplace) /opt/otrs/Kernel/Language/
%dir /opt/otrs/Kernel/Config/
%dir /opt/otrs/Kernel/Output/HTML/
%exclude /opt/otrs/Kernel/cpan-lib*
#/opt/otrs/Kernel/Config/Modules.pm
/opt/otrs/Kernel/Config/Defaults.pm
/opt/otrs/Kernel/Language.pm
/opt/otrs/Kernel/Modules/
/opt/otrs/Kernel/Output/HTML/*.pm
/opt/otrs/Kernel/System/
/opt/otrs/scripts/

%defattr(-, otrs, apache)
%dir /opt/otrs/
%config(noreplace) /opt/otrs/.procmailrc
%config(noreplace) /opt/otrs/.fetchmailrc
%config(noreplace) /opt/otrs/.mailfilter
%config(noreplace) /opt/otrs/var/log/TicketCounter.log
%config(noreplace) /opt/otrs/var/cron/*
/opt/otrs/var/article/
/opt/otrs/var/httpd/
/opt/otrs/var/spool/
/opt/otrs/var/tmp/
/opt/otrs/var/pics/stats/

%defattr(-, apache, apache)
/opt/otrs/var/sessions/

%defattr(-, otrs, root, 0755)
/opt/otrs/bin/*

%files docs
%defattr(-, root, root, 0755)
%doc doc/

%changelog
* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.4-1.2
- Rebuild for Fedora Core 5.

* Sat Apr 15 2006 Dag Wieers <dag@wieers.com> - 2.0.4-2
- Added missing perl-Apache-DBI dependency. (Grant McChesney)

* Sun Nov 27 2005 Dries Verachtert <dries@ulyssis.org> - 2.0.4-1
- Updated to release 2.0.4.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 2.0.3-1
- Updated to release 2.0.3.

* Wed Jul 14 2004 Dag Wieers <dag@wieers.com> - 1.2.4-1
- Updated to release 1.2.4.

* Wed Apr 14 2004 Dag Wieers <dag@wieers.com> - 1.2.3-2
- Require smtpdaemon instead of sendmail.

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 1.2.3-1
- Updated to release 1.2.3.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Cosmetic rebuild for Group-tag and BuildArch-tag.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 1.2.2-0
- Updated to release 1.2.2.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 1.2.2-0
- Updated to release 1.2.2.

* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 1.2.1-0
- Initial package. (using DAR)
