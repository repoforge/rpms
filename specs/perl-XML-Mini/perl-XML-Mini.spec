# $Id$
# Authority: dries
# Upstream: Pat Deegan <pause$psychogenic,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Mini

Summary: MiniXML XML generator and parser interface
Name: perl-XML-Mini
Version: 1.2.8
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Mini/

Source: http://search.cpan.org/CPAN/authors/id/P/PD/PDEEGAN/XML-Mini-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
XML::Mini is a set of Perl (and PHP) classes that allow you to access
XML data and create valid XML output with a tree-based hierarchy of
elements.

It provides an easy, object-oriented interface for manipulating XML
documents and their elements. It is currently being used to send
requests and understand responses from remote servers in Perl or PHP
applications.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/Mini.pm
%{perl_vendorlib}/XML/Mini

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.8-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.8-1
- Initial package.
