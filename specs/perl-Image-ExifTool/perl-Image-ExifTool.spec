# $Id$
# Authority: dries
# Upstream: Phil Harvey <phil%20at%20owl,phy,queensu,ca>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-ExifTool

Summary: Read and write meta information in images
Name: perl-Image-ExifTool
Version: 5.87
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-ExifTool/

Source: http://search.cpan.org/CPAN/authors/id/E/EX/EXIFTOOL/Image-ExifTool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
ExifTool is a highly customizable Perl script for reading and writing meta
information in images.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/exiftool
%{perl_vendorlib}/File/RandomAccess.p*
%{perl_vendorlib}/Image/ExifTool.p*
%{perl_vendorlib}/Image/ExifTool/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 5.87-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 5.87-1
- Updated to release 5.87.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 5.77-1
- Initial package.
