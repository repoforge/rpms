# $Id$
# Authority: dries
# Upstream: Slaven Rezi&#263; <slaven$rezic,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tk-FontDialog

Summary: Font dialog widget for perl/Tk
Name: perl-Tk-FontDialog
Version: 0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tk-FontDialog/

Source: http://search.cpan.org/CPAN/authors/id/S/SR/SREZIC/Tk-FontDialog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Tk::FontDialog is a font chooser for perl/Tk. 

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
%{perl_vendorlib}/Tk/FontDialog.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
