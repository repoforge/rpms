# $Id$
# Authority: dries
# Upstream: David Muir Sharnoff <muir$idiom,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-CRC

Summary: Cyclic redundency check generation
Name: perl-String-CRC
Version: 1.0
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-CRC/

Source: http://search.cpan.org/CPAN/authors/id/M/MU/MUIR/modules/String-CRC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
The CRC module calculates CRC of various lenghts. The default CRC length is
32 bits.
CRCs of 32 bits and smaller will be returned as an integer.
CRCs that are larger than 32 bits will be returned as two integers if called
in list context and as a packed binary string if called in scalar context.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/String/
%{perl_vendorarch}/String/CRC.pm
%{perl_vendorarch}/String/CRC.pod
%dir %{perl_vendorarch}/auto/String/
%{perl_vendorarch}/auto/String/CRC/

%changelog
* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
