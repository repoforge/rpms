# $Id$
# Authority: dries
# Upstream: Rani Pinchuk <rani%20at%20cpan%20dot%20org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Regexp-Ignore

Summary: Let us ignore unwanted parts, while parsing text
Name: perl-Regexp-Ignore
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Regexp-Ignore/

Source: http://search.cpan.org/CPAN/authors/id/R/RA/RANI/Regexp-Ignore-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Let us ignore unwanted parts, while parsing text.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Regexp/Ignore.pm
%{perl_vendorlib}/Regexp/IgnoreHTML.pm
%{perl_vendorlib}/Regexp/IgnoreTextCharacteristicsHTML.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
