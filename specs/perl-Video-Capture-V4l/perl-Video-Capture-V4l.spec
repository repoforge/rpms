# $Id$
# Authority: dries
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Video-Capture-V4l

Summary: Perl interface to the Video4linux framegrabber interface
Name: perl-Video-Capture-V4l
Version: 0.901
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Video-Capture-V4l/

Source: http://www.cpan.org/modules/by-module/Video/Video-Capture-V4l-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl interface to the Video4linux framegrabber interface.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST META.yml README TODO examples/
%doc %{_mandir}/man3/Video::Capture::V4l.3pm*
%doc %{_mandir}/man3/Video::Capture::VBI.3pm*
%doc %{_mandir}/man3/Video::Frequencies.3pm*
%doc %{_mandir}/man3/Video::RTjpeg.3pm*
%doc %{_mandir}/man3/Video::XawTV.3pm*
%dir %{perl_vendorarch}/auto/Video/
%dir %{perl_vendorarch}/auto/Video/Capture/
%{perl_vendorarch}/auto/Video/Capture/V4l/
%{perl_vendorarch}/auto/Video/Capture/VBI/
%{perl_vendorarch}/auto/Video/RTjpeg/
%dir %{perl_vendorarch}/Video/
%dir %{perl_vendorarch}/Video/Capture/
%{perl_vendorarch}/Video/Capture/VBI.pm
%{perl_vendorarch}/Video/Capture/V4l.pm
%{perl_vendorarch}/Video/Frequencies.pm
%{perl_vendorarch}/Video/RTjpeg.pm
%{perl_vendorarch}/Video/XawTV.pm

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.901-1
- Updated to release 0.901.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.225-1
- Initial package.
