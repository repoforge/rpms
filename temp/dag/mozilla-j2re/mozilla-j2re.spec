# Authority: dag

Summary: JRE link for Mozilla.
Name: mozilla-j2re
Version: 1.4.2
Release: 2
License: GPL
Group: Applications/Internet
URL: http://dag.wieers.com/packages/mozilla-j2re/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
Requires: j2re = %{version}
Requires: mozilla >= 1.3

%description
This packages adds a link needed to get SUN's Java Runtime Environment (JRE)
to work with mozilla.

You need to install j2re-%{version} manually prior to installing
this package. You can get j2re-%{version} from:

	http://java.sun.com/j2se/1.4.2/download.html

%prep
%build
%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/mozilla/plugins \
			%{buildroot}%{_libdir}/netscape/plugins
%{?rh90: %{__ln_s} -f %{_prefix}/java/j2re%{version}/plugin/i386/ns610-gcc32/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}
%{?rh80: %{__ln_s} -f %{_prefix}/java/j2re%{version}/plugin/i386/ns610-gcc32/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}
%{?rh73: %{__ln_s} -f %{_prefix}/java/j2re%{version}/plugin/i386/ns610/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}
%{?rh62: %{__ln_s} -f %{_prefix}/java/j2re%{version}/plugin/i386/ns610/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}
%{__ln_s} -f %{_prefix}/java/j2re%{version}/plugin/i386/ns4/libjavaplugin.so %{buildroot}%{_libdir}/netscape/plugins/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/mozilla/plugins/*
%{_libdir}/netscape/plugins/*

%changelog
* Mon Jul 07 2003 Dag Wieers <dag@wieers.com> - 1.4.2-2
- Updated to j2re release 1.4.2.

* Sat May 10 2003 Dag Wieers <dag@wieers.com> - 1.4.2-1.beta
- Added netscape plugin for older netscape versions.
- Initial package. (using DAR)
- Idea originated from Alexandre Oliva.
