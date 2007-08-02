# $Id$
# Authority: dries
# Upstream: Robin Berjon <robin$knowscape,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Filter-BufferText

Summary: Simple filter which puts all characters into a single event
Name: perl-XML-Filter-BufferText
Version: 1.01
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Filter-BufferText/

Source: http://www.cpan.org/modules/by-module/XML/XML-Filter-BufferText-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This is a very simple filter. One common cause of grief (and programmer
error) is that XML parsers aren't required to provide character events in
one chunk. They can, but are not forced to, and most don't. This filter does
the trivial but oft-repeated task of putting all characters into a single
event.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/Filter/
%{perl_vendorlib}/XML/Filter/BufferText.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
