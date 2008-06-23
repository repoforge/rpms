# $Id$
# Authority: dries
# Upstream: Father Chrysostomos <sprout$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Font-GlyphNames

Summary: Convert between glyph names and characters
Name: perl-Font-GlyphNames
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Font-GlyphNames/

Source: http://www.cpan.org/modules/by-module/Font/Font-GlyphNames-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Convert between glyph names and characters.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Font::GlyphNames.3pm*
%dir %{perl_vendorlib}/Font/
%{perl_vendorlib}/Font/GlyphNames/
%{perl_vendorlib}/Font/GlyphNames.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.03-1
- Updated to release 0.03.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
