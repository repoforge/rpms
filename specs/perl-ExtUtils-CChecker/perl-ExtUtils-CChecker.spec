# $Id$
# Upstream: Paul Evans <leonerd@leonerd.org.uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name ExtUtils-CChecker

Summary: configure-time utilities for using C headers, libraries, or OS features
Name: perl-ExtUtils-CChecker
Version: 0.02
Release: 1%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-CChecker

Source: http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/ExtUtils-CChecker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
Requires: perl(ExtUtils::CBuilder)

%filter_from_requires /^perl*/d
%filter_setup

%description
Often Perl modules are written to wrap functionallity found in existing C headers, libraries, or to use OS-specific features. It is useful in the Build.PL or Makefile.PL file to check for the existance of these requirements before attempting to actually build the module.

Objects in this class provide an extension around ExtUtils::CBuilder to simplify the creation of a .c file, compiling, linking and running it, to test if a certain feature is present.

It may also be necessary to search for the correct library to link against, or for the right include directories to find header files in. This class also provides assistance here.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}
%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README 
%doc %{_mandir}/man3/ExtUtils::CChecker.3pm*
%{perl_vendorlib}/ExtUtils/CChecker.pm

%changelog
* Wed Feb 03 2010 Christoph Maser <cmr@financial.com> - 0.02
- initial package


