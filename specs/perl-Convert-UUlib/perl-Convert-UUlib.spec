# $Id$
# Authority: dag

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-UUlib

Summary: Perl interface to the uulib library
Name: perl-Convert-UUlib
Version: 1.051
Release: 1.2
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-UUlib/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-UUlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.8.0
Requires: perl >= 0:5.8.0

%description
A perl interface to the uulib library (a.k.a. uudeview/uuenview).

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot (arch)
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes COPYING* doc/* MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/Convert/
%{perl_vendorarch}/auto/Convert/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.051-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 24 2005 Dag Wieers <dag@wieers.com> - 1.051-1
- Updated to release 1.051.

* Sun Feb 20 2005 Dag Wieers <dag@wieers.com> - 1.03-2
- Cosmetic changes.

* Wed Apr 28 2004 Dag Wieers <dag@wieers.com> - 1.03-1
- Updated to release 1.03.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 1.01-0
- Updated to release 1.01.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.31-0
- Updated to release 0.31.
- Initial package. (using DAR)
