# $Id$
# Authority: dries
# Upstream: Rodolphe Ortalo <ortalo$laas,fr>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MOP

Summary: Meta-object protocol for Perl modules
Name: perl-MOP
Version: 1.00
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MOP/

Source: http://www.cpan.org/modules/by-module/MOP/MOP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The two modules MOP::MOP and MOP::MetaModule provide the basis of
a meta-object protocol (MOP) for Perl5 objects.
Basically, a MOP allows trapping of the various method calls made by a
user on the objects he has created from a MOP-aware module. These
method calls are then redirected to another object, called the meta-object,
for further processing. Once the meta-object has taken control of the
method call, it can complement the processing made by the base level
target object in various ways. Possible applications include:
transparent remote invocation, authentication, replicas management or
stable storage for fault tolerance, etc.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/MOP

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.00-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
