# $Id$
# Authority: dag
# Upstream: Torsten Schönfeld <kaffeetisch$gmx,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GStreamer

Summary: Perl module with bindings to the GStreamer library
Name: perl-GStreamer
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GStreamer/

Source: http://www.cpan.org/modules/by-module/GStreamer/GStreamer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: gstreamer-devel >= 0.10
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Glib)
Requires: perl

%description
GStreamer is a Perl module with bindings to the GStreamer library.

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
%doc ChangeLog LICENSE MANIFEST MANIFEST.SKIP META.yml NEWS README TODO copyright.pod examples/
%doc %{_mandir}/man3/GStreamer.3pm*
%doc %{_mandir}/man3/GStreamer::*.3pm*
%{perl_vendorarch}/auto/GStreamer/
%{perl_vendorarch}/GStreamer/
%{perl_vendorarch}/GStreamer.pm

%changelog
* Sat May 10 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
