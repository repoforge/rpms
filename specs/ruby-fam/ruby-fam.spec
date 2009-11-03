# $Id$
# Authority: dag

%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")

%define real_name fam-ruby

Summary: Gamin/FAM bindings for Ruby
Name: ruby-fam
Version: 0.2.0
Release: 1%{?dist}
License: BSD
Group: Development/Languages
URL: http://www.pablotron.org/software/fam-ruby/

Source: http://www.pablotron.org/download/fam-ruby-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ruby, ruby-devel >= 1.8, gamin-devel
Requires: ruby >= 1.8
Provides: ruby(fam) = 0.1.4
Provides: ruby(gamin) = 0.1.4

%description
FAM-Ruby is a Ruby interface to SGI's File Alteration Monitor
(http://oss.sgi.com/projects/fam/).  FAM allows you to monitor files and
directories for changes (file modification, creation, and removal) -- in
an event-driven manner.

%prep
%setup -n %{real_name}-%{version}
%{__mv} -f doc/ api/

%build
export CFLAGS="%{optflags}"
ruby extconf.rb
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
 
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README *.txt api/
%{ruby_sitearch}/fam.so

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.2.0-1
- Initial package. (using DAR)
