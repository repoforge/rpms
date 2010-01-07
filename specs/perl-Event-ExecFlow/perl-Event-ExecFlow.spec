# $Id$
# Authority: matthias
# Upstream: Jörn Reder <joern$zyn,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Event-ExecFlow

Summary: High level API for event-based execution flow control
Name: perl-Event-ExecFlow
Version: 0.64
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://www.exit1.org/Event-ExecFlow/

Source: http://search.cpan.org/CPAN/authors/id/J/JR/JRED/Event-ExecFlow-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(AnyEvent) >= 0.4
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Locale::TextDomain)
BuildRequires: perl(Test::More)
Requires: perl(AnyEvent) >= 0.4
Requires: perl(Locale::TextDomain)
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup

%description
Event::ExecFlow offers a high level API to declare jobs, which mainly execute
external commands, parse their output to get progress or other status
information, triggers actions when the command has been finished etc. Such jobs
can be chained together in a recursive fashion to fulfill rather complex tasks
which consist of many jobs.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
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
* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 0.64-1
- Updated to version 0.64.

* Thu May 31 2007 Matthias Saou <http://freshrpms.net/> 0.63-2
- Build require perl(ExtUtils::MakeMaker) for F7.

* Mon Apr 16 2007 Matthias Saou <http://freshrpms.net/> 0.63-1
- Update to 0.63.

* Mon Jun 19 2006 Matthias Saou <http://freshrpms.net/> 0.62-1
- Update to 0.62.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 0.61-1
- Initial RPM release.

