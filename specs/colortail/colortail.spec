# $Id$
# Authority: dag
# Upstream: Joakim Andersson <ja$morrdusk,net>

%{?dist: %{expand: %%define %dist 1}}

Summary: Log colorizer that makes log checking easier
Name: colortail
Version: 0.3.0
Release: 1
Group: Applications/File
License: GPL
URL: http://www.student.hk-r.se/~pt98jan/colortail.html

Source: http://www.student.hk-r.se/~pt98jan/colortail-%{version}.tar.gz
Patch: colortail-0.3.0-gcc3.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Colortail is a log colorizer that makes log checking easier. It works
like tail but can read one or more configuration files. In which it's
specified which patterns result in which colors. 

%prep
%setup
%{!?rh6:%patch0 -b .gcc3}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO example-conf/conf.*
%{_bindir}/colortail

%changelog
* Mon Apr 04 2005 Dag Wieers <dag@wieers.com> - 0.3.0-1
- Added example config files. (Adrian Reber)

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.3.0-0
- Initial package. (using DAR)
