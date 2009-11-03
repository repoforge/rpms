# $Id$
# Authority: dries
# Upstream: Abigail <$cpan$$abigail,be>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geography-States

Summary: Map states and provinces to their codes and vica versa
Name: perl-Geography-States
Version: 2009040901
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geography-States/

Source: http://www.cpan.org/modules/by-module/Geography/Geography-States-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Map states and provinces to their codes, and vica versa.

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
%doc %{_mandir}/man3/Geography::States*
%{perl_vendorlib}/Geography/States.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 2009040901-1
- Updated to version 2009040901.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Initial package.
