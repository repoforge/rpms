# $Id$
# Authority: dfateyev
# Upstream: Paul P Komkoff Jr <i$stingr,net> 

Name:           rzip
Version:        2.1
Release:        1%{?dist}
Summary:        A large-file compression program
Group:          Applications/File
License:        GPL
URL:            http://rzip.samba.org
Source0:        http://rzip.samba.org/ftp/rzip/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  bzip2-devel


%description
rzip is a compression program, similar in functionality to gzip or
bzip2, but able to take advantage of long distance redundancies in
files, which can sometimes allow rzip to produce much better
compression ratios than other programs.


%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_BIN="%{buildroot}/%{_bindir}" INSTALL_MAN="%{buildroot}/%{_mandir}"

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/rzip
%{_mandir}/man1/*


%changelog
* Tue Mar 01 2011 Denis Fateyev <denis@fateyev.com> - 2.1-1
- Initial release, thanks to Dan Pritts <danno@internet2.edu> for specs.

