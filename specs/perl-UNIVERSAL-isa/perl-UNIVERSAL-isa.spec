# $Id$
# Authority: dries
# Upstream: &#1497;&#1493;&#1489;&#1500; &#1511;&#1493;&#1490;'&#1502;&#1503; <nothingmuch$woobling,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIVERSAL-isa

Summary: Hack around people using UNIVERSAL::isa
Name: perl-UNIVERSAL-isa
Version: 1.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIVERSAL-isa/

Source: http://www.cpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-isa-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(Scalar::Util)

%description
Hack around module authors using UNIVERSAL::isa as a function when they shouldn't.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%{perl_vendorlib}/UNIVERSAL/isa.pm

%changelog
* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 1.03-1
- Updated to version 1.03.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1.2
- Rebuild for Fedora Core 5.

* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
