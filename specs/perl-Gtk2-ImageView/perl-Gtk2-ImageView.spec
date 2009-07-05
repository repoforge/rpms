# $Id$
# Authority: dag
# Upstream: Jeffrey Ratcliffe

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2-ImageView

Summary: Perl bindings for the GtkImageView widget
Name: perl-Gtk2-ImageView
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2-ImageView/

Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-ImageView-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel
BuildRequires: gtkimageview-devel
BuildRequires: perl
BuildRequires: perl(Cairo::Install::Files)
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Glib)
BuildRequires: perl(Gtk2)
Requires: gtk2

%description
Perl bindings for the GtkImageView widget.

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
%doc AUTHORS COPYING.LESSER INSTALL MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Gtk2::Gdk::Pixbuf::Draw::Cache.3pm*
%doc %{_mandir}/man3/Gtk2::ImageView.3pm*
%doc %{_mandir}/man3/Gtk2::ImageView::*.3pm*
%dir %{perl_vendorarch}/auto/Gtk2/
%{perl_vendorarch}/auto/Gtk2/ImageView/
%dir %{perl_vendorarch}/Gtk2/
%dir %{perl_vendorarch}/Gtk2/Gdk/
%dir %{perl_vendorarch}/Gtk2/Gdk/Pixbuf/
%dir %{perl_vendorarch}/Gtk2/Gdk/Pixbuf/Draw/
%{perl_vendorarch}/Gtk2/Gdk/Pixbuf/Draw/Cache.pod
%{perl_vendorarch}/Gtk2/ImageView/
%{perl_vendorarch}/Gtk2/ImageView.pm
%{perl_vendorarch}/Gtk2/ImageView.pod

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.05-1
- Updated to version 0.05.

* Tue Dec 09 2008 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
