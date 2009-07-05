# $Id$
# Authority: dag
# Upstream: Maintained by Ken Williams <KWILLIAMS$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Spec

Summary: Tools for working with paths and file specs across platforms
Name: perl-File-Spec
Version: 3.30
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Spec/

Source: http://www.cpan.org/modules/by-module/File/PathTools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(File::Path)
BuildRequires: perl(Module::Build) >= 0.19
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test)
Requires: perl >= 0:5.005

%description
Tools for working with paths and file specs across platforms.

%prep
%setup -n PathTools-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL MANIFEST META.yml SIGNATURE
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/File/
%{perl_vendorarch}/Cwd.pm
%{perl_vendorarch}/File/Spec/
%{perl_vendorarch}/File/Spec.pm
%{perl_vendorarch}/auto/Cwd/

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 3.30-1
- Updated to version 3.30.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 3.25-1
- Initial package. (using DAR)
