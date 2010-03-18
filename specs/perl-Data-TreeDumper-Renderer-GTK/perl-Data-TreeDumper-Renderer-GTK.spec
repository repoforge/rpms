# $Id$
# Authority: shuff
# Upstream: Khemir Nadim ibn Hamouda <nadim$khemir,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-TreeDumper-Renderer-GTK

Summary: Gtk2::TreeView renderer for Data::TreeDumper
Name: perl-%{real_name}
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-TreeDumper-Renderer-GTK/

Source: http://search.cpan.org/CPAN/authors/id/N/NK/NKH/Data-TreeDumper-Renderer-GTK-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Cairo)
BuildRequires: perl(Data::TreeDumper) >= 0.33
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Glib)
BuildRequires: perl(Gtk2)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Cairo)
Requires: perl(Data::TreeDumper) >= 0.33
Requires: perl(Glib)
Requires: perl(Gtk2)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This widget is the gui equivalent of Data::TreeDumper; it will display a perl
data structure in a TreeView, allowing you to fold and unfold child data
structures and get a quick feel for what's where. Right-clicking anywhere in
the view brings up a context menu, from which the user can choose to expand or
collapse all items.

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
%doc Changes MANIFEST README Todo
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Data/TreeDumper/Renderer/
%{perl_vendorlib}/Data/TreeDumper/Renderer/*
%{perl_vendorlib}/auto/Data/TreeDumper/Renderer/*

%changelog
* Thu Mar 18 2010 Steve Huff <shuff@vecna.org> - 0.02-1
- Initial version.
