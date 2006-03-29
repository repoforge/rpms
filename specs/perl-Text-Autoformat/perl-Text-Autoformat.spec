# $Id$

# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define real_name Text-Autoformat
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Automatic text wrapping and reformatting
Name: perl-Text-Autoformat
Version: 1.13
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Autoformat/

Source: http://www.cpan.org/modules/by-module/Text/Text-Autoformat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Text::Autoformat provides intelligent formatting of
plaintext without the need for any kind of embedded mark-up. The module
recognizes Internet quoting conventions, a wide range of bulleting and
number schemes, centred text, and block quotations, and reformats each
appropriately. Other options allow the user to adjust inter-word
and inter-paragraph spacing, justify text, and impose various
capitalization schemes.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Autoformat.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Initial package.
