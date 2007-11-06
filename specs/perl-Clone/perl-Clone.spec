# $Id$
# Authority: dries
# Upstream: Ray Finch <finchray$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Clone

Summary: Recursively copy Perl datatypes
Name: perl-Clone
Version: 0.22
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Clone/

Source: http://www.cpan.org/modules/by-module/Clone/Clone-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
With this module, you can recursively copy Perl datatypes.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Clone.pm
%{perl_vendorarch}/auto/Clone/

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Initial package.
