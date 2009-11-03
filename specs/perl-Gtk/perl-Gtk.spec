# $Id$
# Authority: dag
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk
%define real_version 0.7009

Summary: Perl module providing GTK bindings
Name: perl-Gtk
Version: 0.7009
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk/

Source: http://www.cpan.org/modules/by-module/Gtk/Gtk-Perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Gtk is a Perl module providing GTK bindings.

%prep
%setup -n %{real_name}-Perl-%{version}

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
%doc ChangeLog INSTALL MANIFEST NOTES README VERSIONS
%doc %{_mandir}/man3/Gtk.3pm*
#%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/Gtk.pm
%{perl_vendorarch}/auto/Gtk/

%changelog
* Sun May 27 2007 Dag Wieers <dag@wieers.com> - 0.7009-1
- Initial package. (using DAR)
