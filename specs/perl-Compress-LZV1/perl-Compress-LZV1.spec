# $Id$
# Authority: dries
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-LZV1

Summary: Extremely leight-weight Lev-Zimpel-Vogt compression
Name: perl-Compress-LZV1
Version: 0.04
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-LZV1/

Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/Compress-LZV1-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
LZV1 is an extremely fast (not that much slower than a pure memcpy)
compression algorithm. It is ideal for applications where you want to
save *some* space but not at the cost of speed. It is ideal for
repetitive data as well. The module is self-contained and very small (no
large library to be pulled in).

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
%{perl_vendorarch}/Compress/LZV1.pm
%{perl_vendorarch}/auto/Compress/LZV1

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
