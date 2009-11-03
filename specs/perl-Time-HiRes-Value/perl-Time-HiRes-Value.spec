# $Id$
# Authority: dries
# Upstream: Paul Evans <leonerd$leonerd,org,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-HiRes-Value

Summary: Class representing a time value or interval in exact microseconds
Name: perl-Time-HiRes-Value
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-HiRes-Value/

Source: http://www.cpan.org/modules/by-module/Time/Time-HiRes-Value-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)


%description
Class representing a time value or interval in exact microseconds.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST META.yml
%doc %{_mandir}/man3/Time::HiRes::Value.3pm*
%dir %{perl_vendorlib}/Time/
%dir %{perl_vendorlib}/Time/HiRes/
#%{perl_vendorlib}/Time/HiRes/Value/
%{perl_vendorlib}/Time/HiRes/Value.pm

%changelog
* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 0.07-1
- Updated to version 0.07.

* Fri Jul 10 2009 Christoph Maser <cmr@financial.com> - 0.06-1
- Updated to version 0.06.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
