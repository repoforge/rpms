# $Id$
# Authority: dries
# Upstream: Jesse Vincent <jesse+cpan$fsck,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-ReturnValue

Summary: Return-value object
Name: perl-Class-ReturnValue
Version: 0.53
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-ReturnValue/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/Class-ReturnValue-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
A return-value object that lets you treat it as as a boolean, array or object.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Class/ReturnValue.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.53-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Updated to release 0.53.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Initial package.
