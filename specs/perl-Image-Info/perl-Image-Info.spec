# $Id$
# Authority: dries
# Upstream: Tels <nospam-abuse$bloodgate,com>

### EL6 ships with perl-Image-Info-1.28-6.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-Info

Summary: Extract meta information from image files
Name: perl-Image-Info
Version: 1.30
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Info/

Source: http://search.cpan.org/CPAN/authors/id/S/SR/SREZIC/Image-Info-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.2
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
# don't install without at least one of our XML modules
BuildRequires: perl-Image-Info-alternative = %{version}
Requires: perl >= 1:5.6.2
# don't install without at least one of our XML modules
Requires: perl-Image-Info-alternative = %{version}

%filter_from_requires /^perl(XML.*/d
%filter_setup


%description
This Perl extention allows you to extract meta information from
various types of image files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc CHANGES CREDITS MANIFEST MANIFEST.SKIP META.yml README SIGNATURE TODO
%doc %{_mandir}/man3/Image::Info.3pm*
%doc %{_mandir}/man3/Image::Info::*.3pm*
%dir %{perl_vendorlib}/Image/
%{perl_vendorlib}/Image/Info/
%{perl_vendorlib}/Image/Info.pm
%{perl_vendorlib}/Image/TIFF.pm

%changelog
* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 1.30-1
- Updated to version 1.30.

* Thu Sep 10 2009 Christoph Maser <cmr@financial.com> - 1.29-3
- filter perl(XML* dependencies with %filter_from_requires

* Thu Sep 10 2009 Steve Huff <shuff@vecna.org> - 1.29-2
- added dependency on perl-Image-Info-alternative
  currently satisfied by perl-XML-LibXML >= 1.62
  or perl-XML-Simple

* Fri Aug  7 2009 Christoph Maser <cmr@financial.com> - 1.29-1
- Updated to version 1.29.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.28-1
- Updated to release 1.28.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.27-1
- Updated to release 1.27.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.26-1
- Updated to release 1.26.

* Wed Jun 13 2007 Dries Verachtert <dries@ulyssis.org> - 1.25-1
- Updated to release 1.25.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Updated to release 1.24.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Updated to release 1.23.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Updated to release 1.21.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-2
- Fixed the license tag (Thanks to David Necas !)

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Initial package.
