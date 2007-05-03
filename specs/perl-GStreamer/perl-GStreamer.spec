# $Id$
# Authority: dag
# Upstream: Torsten Schönfeld <kaffeetisch$gmx,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GStreamer

Summary: Perl module with bindings to the GStreamer library
Name: perl-GStreamer
Version: 0.09
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GStreamer/

Source: http://www.cpan.org/modules/by-module/GStreamer/GStreamer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, gstreamer-devel >= 0.10
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
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE MANIFEST META.yml NEWS README TODO
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/GStreamer.pm
%{perl_vendorarch}/GStreamer/
%{perl_vendorarch}/auto/GStreamer/

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
