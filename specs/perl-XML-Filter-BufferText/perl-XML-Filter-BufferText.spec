# $Id$

# Authority: dries
# Upstream: Robin Berjon <robin$knowscape,com>

%define real_name XML-Filter-BufferText
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Simple filter which puts all characters into a single event
Name: perl-XML-Filter-BufferText
Version: 1.01
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Filter-BufferText/

Source: http://search.cpan.org/CPAN/authors/id/R/RB/RBERJON/XML-Filter-BufferText-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a very simple filter. One common cause of grief (and programmer
error) is that XML parsers aren't required to provide character events in
one chunk. They can, but are not forced to, and most don't. This filter does 
the trivial but oft-repeated task of putting all characters into a single 
event.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/Filter/BufferText.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
