# Authority: dag

%define rversion 1.2.2-01

Summary: Open Ticket Request System.
Name: otrs
Version: 1.2.2
Release: 0
License: GPL
Group: Applications/Internet
URL: http://otrs.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.otrs.org/pub/otrs/otrs-%{rversion}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

#Autoreqprov:  no
Requires: perl, perl-DBI, perl-DBD-MySQL, perl-URI, mod_perl
Requires: mysql, mysql-server, fetchmail, procmail, sendmail
%{?rhfc1:BuildRequires: httpd}
%{?rhel3:BuildRequires: httpd}
%{?rh90:BuildRequires: httpd}
%{?rh80:BuildRequires: httpd}
%{?rh73:BuildRequires: apache}
%{?rhel21:BuildRequires: apache}
%{?rh62:BuildRequires: apache}

%description
OTRS is an Open source Ticket Request System with many features to manage
customer telephone calls and e-mails.

%package docs
Summary: Documentation for package %{name}.
Group: Documentation

%description docs
OTRS is an Open source Ticket Request System with many features to manage
customer telephone calls and e-mails.

This package includes the documentation for %{name}.
  
%prep
%setup -n %{name}

%{__mv} -f Kernel/Config.pm.dist Kernel/Config.pm

for file in Kernel/Config/*.dist; do
	%{__mv} -f $file Kernel/Config/$(basename $file .dist)
done

for file in var/cron/*.dist; do
	%{__mv} -f $file var/cron/$(basename $file .dist)
done

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_initrddir} \
			%{buildroot}%{_sysconfdir}/sysconfig/ \
			%{buildroot}%{_sysconfdir}/httpd/conf.d/ \
			%{buildroot}/opt/otrs/

### Copy everything.
%{__cp} -avf Kernel/ bin/ scripts/ var/ %{buildroot}/opt/otrs/

### Copy with permissions.
%{__install} -m0710 .fetchmailrc %{buildroot}/opt/otrs/
%{__install} -m0644 .procmailrc %{buildroot}/opt/otrs/
%{__install} -m0600 .mailfilter %{buildroot}/opt/otrs/
%{__install} -m0700 bin/DeleteSessionIDs.pl bin/UnlockTickets.pl bin/otrs.getConfig %{buildroot}/opt/otrs/bin/

### Copy extra configuration files.
%{__install} -m0755 scripts/redhat-rcotrs %{buildroot}%{_initrddir}/otrs
%{__install} -m0644 scripts/redhat-rcotrs-config %{buildroot}%{_sysconfdir}/sysconfig/otrs
%{__install} -m0644 scripts/apache2-httpd.include.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/otrs.conf

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
%doc CHANGES COPYING INSTALL* README* UPGRADING TODO
%config(noreplace) %{_sysconfdir}/sysconfig/otrs
%config(noreplace) %{_sysconfdir}/httpd/conf.d/otrs.conf
%config %{_initrddir}/otrs
%config(noreplace) /opt/otrs/Kernel/Config.pm
%config(noreplace) /opt/otrs/Kernel/Config/GenericAgent.pm*
%config(noreplace) /opt/otrs/Kernel/Config/ModulesCusto*.pm
%config(noreplace) /opt/otrs/Kernel/Output/HTML/Standard/
%config(noreplace) /opt/otrs/Kernel/Output/HTML/Lite/
%config(noreplace) /opt/otrs/Kernel/Language/
%dir /opt/otrs/Kernel/Config/
%dir /opt/otrs/Kernel/Output/HTML/
/opt/otrs/Kernel/cpan-lib*
/opt/otrs/Kernel/Config/Modules.pm
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
* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 1.2.2-0
- Updated to release 1.2.2.

* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 1.2.1-0
- Initial package. (using DAR)
