# $Id$
# Authority: dries
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-LZF

Summary: Extremely light-weight Lev-Zimpel-Free compression
Name: perl-Compress-LZF
Version: 1.51
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-LZF/

Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/Compress-LZF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
LZF is an extremely fast (not that much slower than a pure memcpy)
compression algorithm. It is ideal for applications where you want to
save *some* space but not at the cost of speed. It is ideal for
repetitive data as well. The module is self-contained and very small (no
large library to be pulled in). It is also free, so there should be no
problems incoporating this module into commercial programs.
	
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
%{perl_vendorarch}/Compress/LZF.pm
%{perl_vendorarch}/auto/Compress/LZF

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.51-1
- Updated to release 1.51.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Initial package.
