# $Id$
# Upstream: Matija Grabnar <matija,grabnar$arnes,si>

%define real_name File-Tail
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Perl extension for reading from continuosly updated files
Name: perl-File-Tail
Version: 0.98
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Tail/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/M/MG/MGRABNAR/File-Tail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The File::Tail module is designed for reading files which are continously
appended to (the name comes from the tail -f directive). Usualy such files are
logfiles of some description.

The module tries hard not to busy wait on the file, dynamicaly calcultaing 
how long it should wait before it pays to try reading the file again.

The module should handle normal log truncations ("close; move; open"
or "cat /dev/null >file") transparently, without losing any input.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/File/
%{perl_vendorlib}/auto/File/

%changelog
* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.98-1
- Changed to noarch package.
- Cleanup and cosmetic changes.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.98-1
- Initial package.
