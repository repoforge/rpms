# $Id$
# Authority: dries
# Upstream: Benjamin Trott <cpan$stupidfool,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Buffer

Summary: Read/write buffer class
Name: perl-Data-Buffer
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Buffer/

Source: http://search.cpan.org/CPAN/authors/id/B/BT/BTROTT/Data-Buffer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Data::Buffer implements a low-level binary buffer in which you can get and
put integers, strings, and other data. Internally the implementation is
based on pack and unpack, such that Data::Buffer is really a layer on top of
those built-in functions.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" "PREFIX=%{buildroot}%{_prefix}"
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
%{perl_vendorlib}/Data/Buffer.pm

%changelog
* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
