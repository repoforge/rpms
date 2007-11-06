# $Id$
# Authority: dries
# Upstream: Rob Seegel <RobSeegel$comcast,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tk-MListbox

Summary: Multicolumn Listbox
Name: perl-Tk-MListbox
Version: 1.11
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tk-MListbox/

Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCS/Tk-MListbox-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Multicolumn Listbox.

%prep
%setup -n MListbox-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes readme
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tk/MListbox.p*
%{perl_vendorlib}/Tk/sql.pl

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Initial package.
