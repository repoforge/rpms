# $Id$
# Authority: matthias
# Upstream: Jörn Reder <joern$zyn,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Event-ExecFlow

Summary: High level API for event-based execution flow control
Name: perl-Event-ExecFlow
Version: 0.62
Release: 1
License: Artistic or GPL
Group: Development/Libraries
URL: http://www.exit1.org/Event-ExecFlow/
Source: http://www.exit1.org/packages/Event-ExecFlow/dist/Event-ExecFlow-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl(AnyEvent)
BuildArch: noarch

%description
Event::ExecFlow offers a high level API to declare jobs, which mainly execute
external commands, parse their output to get progress or other status
information, triggers actions when the command has been finished etc. Such jobs
can be chained together in a recursive fashion to fulfill rather complex tasks
which consist of many jobs.


%prep
%setup -n %{real_name}-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod \
           %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_bindir}/execflow
%{perl_vendorlib}/Event/ExecFlow/
%{perl_vendorlib}/Event/ExecFlow.pm
%{_mandir}/man3/*


%changelog
* Mon Jun 19 2006 Matthias Saou <http://freshrpms.net/> 0.62-1
- Update to 0.62.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 0.61-1
- Initial RPM release.

