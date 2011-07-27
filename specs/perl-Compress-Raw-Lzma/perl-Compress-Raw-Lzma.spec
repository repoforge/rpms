# $Id$
# Authority: shuff
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-Raw-Lzma

Summary: Low-Level Interface to bzip2 compression library
Name: perl-Compress-Raw-Lzma
Version: 2.037
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-Raw-Lzma/

Source: http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/Compress-Raw-Lzma-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: xz-devel

%filter_from_requires /^perl*/d
%filter_setup

%description
Low-Level Interface to lzma compression library.

%prep
%setup -q -n %{real_name}-%{version}

%{__perl} -pi -e 's|^INCLUDE .*|INCLUDE = %{_includedir}|;' config.in
%{__perl} -pi -e 's|^LIB .*|LIB = %{_libdir}|;' config.in

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Compress::Raw::Lzma.3pm*
%dir %{perl_vendorarch}/auto/Compress/
%dir %{perl_vendorarch}/auto/Compress/Raw/
%{perl_vendorarch}/auto/Compress/Raw/Lzma/
%dir %{perl_vendorarch}/Compress/
%dir %{perl_vendorarch}/Compress/Raw/
%{perl_vendorarch}/Compress/Raw/Lzma.pm

%changelog
* Wed Jul 27 2011 Steve Huff <shuff@vecna.org> - 2.037-1
- Initial package.
