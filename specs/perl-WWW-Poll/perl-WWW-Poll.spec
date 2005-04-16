# $Id$
# Authority: dries
# Upstream: Mike Gammon <mgammon$interport,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Poll

Summary: Perl extension to build web polls
Name: perl-WWW-Poll
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Poll/

Source: http://search.cpan.org/CPAN/authors/id/M/MG/MGAMMON/WWW-Poll-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is a simple perl module to allow folks to easily run 
those oh, so popular polls one sees nowadays.  It requires only 
that you create a world-writable (or server-writable) directory 
called "data" with a few files to seed the poll.  I also have a 
couple of example files included (poll.pl & poll_admin.pl).  If
 you run the script and get an error just run poll_admin.pl 
 first to get it going.  
  

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
%{perl_vendorlib}/WWW/Poll.pm
%{perl_vendorlib}/auto/WWW/Poll

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
