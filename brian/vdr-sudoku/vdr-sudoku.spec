%define pname     sudoku
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        0.1.3
Release:        1%{?dist}
Summary:        Sudoku plugin for VDR

Group:          Amusements/Games
License:        GPL
URL:            http://www.toms-cafe.de/vdr/sudoku/
Source0:        http://toms-cafe.de/vdr/sudoku/%{name}-%{version}.tgz
Source1:        %{name}.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47
Requires:       vdr(abi) = %{apiver}

%description
This is a VDR plugin to generate and solve number place puzzles, so
called Sudokus.


%prep
%setup -q -n sudoku-%{version}
for f in HISTORY README ; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f
done


%build
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{plugindir}/libvdr-%{pname}.so.%{apiver}


%changelog
* Sat Feb 24 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-1
- 0.1.3.

* Sun Jan  7 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.1.2-2
- Rebuild for VDR 1.4.5.

* Mon Dec  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.2-1
- First Fedora Extras build.

* Sat Nov  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.2-0.6
- Rebuild for VDR 1.4.4.

* Sat Sep 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.2-0.5
- Rebuild for VDR 1.4.3.

* Sun Aug  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.2-0.4
- Rebuild for VDR 1.4.1-3.

* Fri Jun 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.2-0.3
- Rebuild for VDR 1.4.1.

* Sun Apr 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.2-0.2
- Rebuild for VDR 1.4.0.

* Tue Apr 25 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.2-0.1
- 0.1.2.

* Fri Nov  4 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1.1-0.1
- 0.1.1, Finnish patch applied upstream.

* Tue Nov  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1.0-0.2
- Rebuild for VDR 1.3.35.

* Sat Oct 29 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1.0-0.1
- First build.
