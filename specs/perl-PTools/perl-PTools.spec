# $Id:$
# Upstream: Chris Cobb <no dot spam at ccobb dot net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name PTools

Summary: Tools for Perl Tool Developers
Name: perl-PTools
Version: 0.02
Release: 1%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PTools

Source: http://search.cpan.org/CPAN/authors/id/C/CC/CCOBB/PTools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Carp)
BuildRequires: perl(Date::Format) >= 2.22
BuildRequires: perl(Date::Parse) >= 2.23
BuildRequires: perl(Exporter)
BuildRequires: perl(Fcntl)
BuildRequires: perl(Getopt::Long) >= 2.17
BuildRequires: perl(POSIX)
BuildRequires: perl(Test::More)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
Requires: perl(Carp)
Requires: perl(Date::Format) >= 2.22
Requires: perl(Date::Parse) >= 2.23
Requires: perl(Exporter)
Requires: perl(Fcntl)
Requires: perl(Getopt::Long) >= 2.17
Requires: perl(POSIX)
Requires: perl(Test::More)
Requires: perl(strict)
Requires: perl(warnings)

%filter_from_requires /^perl*/d
%filter_setup

%description
PTools is a collection of Perl Tools for Perl Tool Developers. These meta-tools have evolved over the years to simplify the normal, everyday types of tasks that most scripts, at some point, need to address.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%{perl_vendorlib}/PTools.pm
%{perl_vendorlib}/PTools/Counter.pm
%{perl_vendorlib}/PTools/Date/Format.pm
%{perl_vendorlib}/PTools/Date/Parse.pm
%{perl_vendorlib}/PTools/Debug.pm
%{perl_vendorlib}/PTools/Extender.pm
%{perl_vendorlib}/PTools/Global.pm
%{perl_vendorlib}/PTools/List.pm
%{perl_vendorlib}/PTools/Loader.pm
%{perl_vendorlib}/PTools/Local.pm
%{perl_vendorlib}/PTools/Options.pm
%{perl_vendorlib}/PTools/Passwd.pm
%{perl_vendorlib}/PTools/Proc/Backtick.pm
%{perl_vendorlib}/PTools/Proc/Daemonize.pm
%{perl_vendorlib}/PTools/Proc/Run.pm
%{perl_vendorlib}/PTools/RedirectIO.pm
%{perl_vendorlib}/PTools/String.pm
%{perl_vendorlib}/PTools/Time/Elapsed.pm
%{perl_vendorlib}/PTools/Verbose.pm
%{perl_vendorlib}/PTools/WordWrap.pm
%{perl_vendorarch}/auto/PTools/.packlist
%doc %{_mandir}/man3/PTools.3pm.gz
%doc %{_mandir}/man3/PTools::Counter.3pm.gz
%doc %{_mandir}/man3/PTools::Date::Format.3pm.gz
%doc %{_mandir}/man3/PTools::Date::Parse.3pm.gz
%doc %{_mandir}/man3/PTools::Debug.3pm.gz
%doc %{_mandir}/man3/PTools::Extender.3pm.gz
%doc %{_mandir}/man3/PTools::Global.3pm.gz
%doc %{_mandir}/man3/PTools::List.3pm.gz
%doc %{_mandir}/man3/PTools::Loader.3pm.gz
%doc %{_mandir}/man3/PTools::Local.3pm.gz
%doc %{_mandir}/man3/PTools::Options.3pm.gz
%doc %{_mandir}/man3/PTools::Passwd.3pm.gz
%doc %{_mandir}/man3/PTools::Proc::Backtick.3pm.gz
%doc %{_mandir}/man3/PTools::Proc::Daemonize.3pm.gz
%doc %{_mandir}/man3/PTools::Proc::Run.3pm.gz
%doc %{_mandir}/man3/PTools::RedirectIO.3pm.gz
%doc %{_mandir}/man3/PTools::String.3pm.gz
%doc %{_mandir}/man3/PTools::Time::Elapsed.3pm.gz
%doc %{_mandir}/man3/PTools::Verbose.3pm.gz
%doc %{_mandir}/man3/PTools::WordWrap.3pm.gz
%doc TODO README Changes META.yml MANIFEST

%changelog
* Sat Feb 06 2010 Christoph Maser <cmr@financial.com> - 0.02-1
- initial package
