# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Kwiki

Summary: Kwiki module for perl
Name: perl-Kwiki
Version: 0.39
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
#URL: http://search.cpan.org/dist/Kwiki/
URL: http://www.kwiki.org/

Source: http://www.cpan.org/modules/by-module/Kwiki/Kwiki-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Kwiki is a modular implementation of a Wiki in Perl.

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
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.39-1
- Updated to release 0.39.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Updated to release 0.38.

* Thu Sep 30 2004 Dag Wieers <dag@wieers.com> - 0.33-1
- Initial package. (using DAR)
