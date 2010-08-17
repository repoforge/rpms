# $Id$
# Authority: shuff
# Upstream: Khemir Nadim ibn Hamouda <nadim$khemir,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name App-Asciio

Summary: ASCII diagramming
Name: perl-%{real_name}
Version: 1.02.71
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/App-Asciio/

Source: http://search.cpan.org/CPAN/authors/id/N/NK/NKH/App-Asciio-%{version}.tar.gz
Patch0: perl-App-Asciio_loose.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Algorithm::Diff)
BuildRequires: perl(Clone)
BuildRequires: perl(Compress::Bzip2)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Compare)
BuildRequires: perl(Data::TreeDumper)
BuildRequires: perl(Data::TreeDumper::Renderer::GTK)
BuildRequires: perl(Directory::Scratch)
BuildRequires: perl(Directory::Scratch::Structured)
BuildRequires: perl(Eval::Context)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Glib)
BuildRequires: perl(Gtk2)
BuildRequires: perl(Gtk2::Gdk::Keysyms)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Module::Util)
BuildRequires: perl(Readonly)
BuildRequires: perl(Sub::Exporter)
# BuildRequires: perl(Test::Block)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::NoWarnings)
# BuildRequires: perl(Test::Strict)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(version) >= 0.5
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Algorithm::Diff)
Requires: perl(Clone)
Requires: perl(Compress::Bzip2)
Requires: perl(Cwd)
Requires: perl(Data::Compare)
Requires: perl(Data::TreeDumper)
Requires: perl(Data::TreeDumper::Renderer::GTK)
Requires: perl(Directory::Scratch)
Requires: perl(Directory::Scratch::Structured)
Requires: perl(Eval::Context)
Requires: perl(File::Basename)
Requires: perl(File::Copy)
Requires: perl(File::Slurp)
Requires: perl(File::Spec)
Requires: perl(Glib)
Requires: perl(Gtk2)
Requires: perl(Gtk2::Gdk::Keysyms)
Requires: perl(List::MoreUtils)
Requires: perl(List::Util)
Requires: perl(MIME::Base64)
Requires: perl(Module::Util)
Requires: perl(Readonly)
Requires: perl(Sub::Exporter)
Requires: perl(version) >= 0.5
Requires: perl(DBI) >= 1.20


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This gtk2-perl application allows you to draw ASCII diagrams in a modern (but
simple) graphical application. The ASCII graphs can be saved as ASCII or in a
format that allows you to modify them later.

Sometimes a diagram is worth a lot of text in a source code file. It has always
been painful to do ASCII diagrams by hand.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

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
%doc Changes MANIFEST README Todo.txt
%doc documentation/
%doc %{_mandir}/man?/*
%{_bindir}/*
%dir %{perl_vendorlib}/App/
%{perl_vendorlib}/App/*

%changelog
* Wed Mar 17 2010 Steve Huff <shuff@vecna.org> - 1.02.71-1
- Initial package.
- Added patch to fix loose/lose misspellings.
