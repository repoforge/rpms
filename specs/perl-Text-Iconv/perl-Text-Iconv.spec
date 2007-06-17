# $Id: perl-Text-Iconv 201 2004-06-03 15:24:49Z bert $
# Authority: dag
# Upstream: Michael Piotrowski <mxp$dynalabs,de>

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Iconv

Summary: Text::Iconv perl module
Name: perl-Text-Iconv
Version: 1.4
Release: 1.2
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Iconv/

Source: http://www.cpan.org/modules/by-module/Text/Text-Iconv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker), perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Perl interface to the iconv() codeset conversion function, as
defined by the Single UNIX Specification.

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
%doc Changes README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/Text/
%{perl_vendorarch}/auto/Text/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1.2
- Rebuild for Fedora Core 5.

* Sun Feb 20 2005 Dag Wieers <dag@wieers.com> - 1.4-1
- Improved %%files list.

* Fri May 21 2004 Dag Wieers <dag@wieers.com> - 1.2-0
- Cosmetic cleanup.

* Tue Apr 06 2004 Bert de Bruijn <bert@debruijn.be>
- initial spec (adapted from PLD).

