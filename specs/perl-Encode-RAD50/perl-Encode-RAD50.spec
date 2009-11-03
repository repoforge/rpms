# $Id$
# Authority: dries
# Upstream: Tom Wyant <wyant$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Encode-RAD50

Summary: Convert to and from the Rad50 character set
Name: perl-Encode-RAD50
Version: 0.005
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Encode-RAD50/

Source: http://www.cpan.org/modules/by-module/Encode/Encode-RAD50-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Convert to and from the Rad50 character set.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Encode::RAD50.3pm*
%dir %{perl_vendorlib}/Encode/
#%{perl_vendorlib}/Encode/RAD50/
%{perl_vendorlib}/Encode/RAD50.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.005-1
- Updated to release 0.005.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.003-1
- Initial package.
