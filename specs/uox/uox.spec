# $Id: $

# Authority: dries
# Upstream:

Summary: Ultima online server
Name: uox
Version: 0.97.6.9r
%define mozilla_version 1.6
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.uox3.org/

Source: http://www.uox3.org/files/uox3-source.zip
Source1: ftp://ftp.mozilla.org/pub/mozilla.org/mozilla/releases/mozilla%{mozilla_version}/src/mozilla-source-%{mozilla_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: dos2unix, autoconf, automake, gcc-c++, unzip

%description
todo

%prep
%setup -c

%build
tar xjvf %{SOURCE1} mozilla/js
dos2unix autogen.sh
bash autogen.sh || echo autogen.sh problem
dos2unix configure
chmod +x configure
%configure --enable-debug
dos2unix Makefile
dos2unix depcomp
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc

%changelog
* Fri Apr 30 2004 Dries Verachtert <dries@ulyssis.org> 0.97.6.9r-1
- initial package
