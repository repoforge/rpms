# $Id$
# Authority: dag
# Upstream: Gaal Yahas, C<< <gaal at forum2.org> >>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Best

Summary: Fallbackable module loader
Name: perl-Best
Version: 0.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Best/

Source: http://www.cpan.org/authors/id/G/GA/GAAL/Best-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.6.0

%description
Fallbackable module loader.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/Best.3pm*
#%{perl_vendorlib}/Best/
%{perl_vendorlib}/Best.pm

%changelog
* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 0.12-1
- Updated to version 0.12.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
