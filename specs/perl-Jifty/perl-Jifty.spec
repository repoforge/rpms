# $Id$
# Authority: dag
# Upstream: Jesse Vincent <jesse+cpan$fsck,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jifty

Summary: Perl package that implements an application framework
Name: perl-Jifty
Version: 0.70824
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jifty/

Source: http://www.cpan.org/modules/by-module/Jifty/Jifty-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.3
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.11
Requires: perl >= 2:5.8.3

%description
perl-Jifty is a Perl package that implements an application framework.

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

### Clean up docs
find doc/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changelog MANIFEST MANIFEST.SKIP META.yml README SIGNATURE doc/ examples/
%doc %{_mandir}/man3/Jifty.3pm*
#%{perl_vendorlib}/Jifty/
%{perl_vendorlib}/Jifty.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.70824-1
- Initial package. (using DAR)
