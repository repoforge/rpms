# $Id$

# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

%define real_name XML-RSS-SimpleGen
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Write RSS files
Name: perl-XML-RSS-SimpleGen
Version: 11.11
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RSS-SimpleGen/

Source: http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/XML-RSS-SimpleGen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is for writing RSS files, simply. It transparently handles
all the unpleasant details of RSS, like proper XML escaping, and also
has a good number of Do-What-I-Mean features, like not changing the
modtime on a written-out RSS file if the file content hasn't changed,
and like automatically removing any HTML tags from content you might
pass in.

This module isn't meant to have the full expressive power of RSS;
instead, it provides functions that are most commonly needed by
RSS-writing programs.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README ChangeLog
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML/RSS/SimpleGen.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 11.11-1
- Initial package.
